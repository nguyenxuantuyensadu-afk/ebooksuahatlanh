import { toast } from 'react-hot-toast';
import React, { useState, useEffect, useRef } from 'react';
import { doc, getDoc, setDoc } from 'firebase/firestore';
import { db } from '../lib/firebase';
import { StickyNote, X, Save, Check, Loader2, CloudIcon, CloudUpload, CloudLightning, CloudLightningIcon } from 'lucide-react';
import { AnimatePresence, motion } from 'motion/react';

export default function NotesPanel({ currentUser, activeModuleId }: { currentUser: any, activeModuleId: string }) {
  const [isOpen, setIsOpen] = useState(false);
  const [note, setNote] = useState('');
  const [loading, setLoading] = useState(false);
  const [saving, setSaving] = useState(false);
  const [saved, setSaved] = useState(false);
  const debounceTimerRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    if (isOpen && currentUser) {
      fetchNote();
    }
  }, [isOpen, activeModuleId, currentUser]);

  const fetchNote = async () => {
    setLoading(true);
    try {
      const docRef = doc(db, 'userNotes', `${currentUser.id}_${activeModuleId}`);
      const docSnap = await getDoc(docRef);
      if (docSnap.exists()) {
        setNote(docSnap.data().content || '');
      } else {
        setNote('');
      }
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const handleNoteChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const newValue = e.target.value;
    setNote(newValue);

    if (debounceTimerRef.current) {
      clearTimeout(debounceTimerRef.current);
    }

    setSaving(true);
    setSaved(false);

    debounceTimerRef.current = setTimeout(async () => {
      if (!currentUser) return;
      try {
        await setDoc(doc(db, 'userNotes', `${currentUser.id}_${activeModuleId}`), {
          userId: currentUser.id,
          moduleId: activeModuleId,
          content: newValue,
          updatedAt: new Date().toISOString()
        }, { merge: true });
        setSaving(false);
        setSaved(true);
        toast.success("Ghi chú đã được lưu", { id: "note-save", duration: 2000 });
        
        // Hide saved status after a while
        setTimeout(() => {
          setSaved(false);
        }, 2000);
      } catch (err) {
        console.error(err);
        setSaving(false);
      }
    }, 1000); // Auto-save after 1s of inactivity
  };

  if (!currentUser) return null;

  return (
    <>
      <button 
        onClick={() => setIsOpen(true)}
        className="fixed bottom-6 right-6 lg:bottom-10 lg:right-10 z-30 p-4 bg-amber-500 hover:bg-amber-600 text-white rounded-full shadow-lg shadow-amber-500/30 transition-transform hover:scale-105 active:scale-95 flex items-center justify-center"
        title="Ghi chú bài học"
      >
        <StickyNote size={24} />
      </button>

      <AnimatePresence>
        {isOpen && (
          <>
            <motion.div 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setIsOpen(false)}
              className="fixed inset-0 bg-stone-900/20 backdrop-blur-sm z-40"
            />
            <motion.div 
              initial={{ x: '100%', opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              exit={{ x: '100%', opacity: 0 }}
              transition={{ type: 'spring', damping: 25, stiffness: 200 }}
              className="fixed top-0 right-0 h-full w-full sm:w-[400px] bg-white shadow-2xl z-50 flex flex-col border-l border-stone-200"
            >
              <div className="flex items-center justify-between p-6 border-b border-stone-100 bg-stone-50/50">
                <div className="flex items-center gap-3">
                  <div className="p-2 bg-amber-100 text-amber-600 rounded-lg">
                    <StickyNote size={20} />
                  </div>
                  <h3 className="font-bold text-lg text-stone-900">Ghi Chú Cá Nhân</h3>
                </div>
                <div className="flex items-center gap-2">
                  <AnimatePresence>
                    {saving && (
                      <motion.div 
                        initial={{ opacity: 0, scale: 0.8 }}
                        animate={{ opacity: 1, scale: 1 }}
                        exit={{ opacity: 0, scale: 0.8 }}
                        className="flex items-center gap-1.5 text-xs font-semibold text-stone-400 bg-stone-100 px-2.5 py-1.5 rounded-full"
                      >
                        <Loader2 size={12} className="animate-spin" />
                        Đang lưu
                      </motion.div>
                    )}
                    {saved && !saving && (
                      <motion.div 
                        initial={{ opacity: 0, scale: 0.8 }}
                        animate={{ opacity: 1, scale: 1 }}
                        exit={{ opacity: 0, scale: 0.8 }}
                        className="flex items-center gap-1.5 text-xs font-semibold text-emerald-600 bg-emerald-50 px-2.5 py-1.5 rounded-full"
                      >
                        <Check size={12} />
                        Đã lưu
                      </motion.div>
                    )}
                  </AnimatePresence>
                  <button 
                    onClick={() => setIsOpen(false)}
                    className="p-2 text-stone-400 hover:text-stone-900 hover:bg-stone-200 rounded-xl transition-colors ml-1"
                  >
                    <X size={20} />
                  </button>
                </div>
              </div>

              <div className="flex-1 p-6 overflow-hidden flex flex-col bg-stone-50/30">
                {loading ? (
                  <div className="flex-1 flex items-center justify-center text-stone-400">
                    <Loader2 size={24} className="animate-spin" />
                  </div>
                ) : (
                  <textarea 
                    value={note}
                    onChange={handleNoteChange}
                    placeholder="Nhập ghi chú của bạn cho phần này..."
                    className="flex-1 w-full p-4 bg-transparent resize-none focus:outline-none text-stone-700 leading-relaxed custom-scrollbar placeholder:text-stone-400"
                  />
                )}
              </div>
              
              <div className="p-4 border-t border-stone-100 bg-white">
                <p className="text-center text-xs font-medium text-stone-400 flex items-center justify-center gap-2">
                  Ghi chú tự động lưu trên thiết bị của bạn
                </p>
              </div>
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </>
  );
}

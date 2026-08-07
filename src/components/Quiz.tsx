import React, { useState, useEffect } from 'react';
import { CheckCircle2, XCircle } from 'lucide-react';
import { doc, getDoc, setDoc } from 'firebase/firestore';
import { db } from '../lib/firebase';
import { toast } from 'react-hot-toast';

interface QuizQuestion {
  question: string;
  options: string[];
  correctAnswerIndex: number;
}

const moduleQuizzes: Record<string, QuizQuestion[]> = {
  nutrition: [
    {
      question: "Nhóm hạt nào sau đây cung cấp năng lượng và độ béo ngậy cho sữa?",
      options: ["Hạt sen, Đậu xanh", "Macca, Óc chó, Hạnh nhân", "Kỷ tử, Táo đỏ", "Yến mạch, Gạo lứt"],
      correctAnswerIndex: 1
    },
    {
      question: "Nguyên tắc quan trọng khi ngâm hạt là gì?",
      options: ["Nước ngâm hạt có thể dùng để nấu sữa", "Không cần rửa hạt trước khi ngâm", "Nước ngâm hạt phải đổ bỏ đi", "Luôn ngâm hạt bằng nước nóng"],
      correctAnswerIndex: 2
    }
  ],
  equipment: [
    {
      question: "Máy làm sữa hạt nào phù hợp cho mô hình kinh doanh nhỏ?",
      options: ["Máy ép chậm", "Máy xay sinh tố thông thường", "Máy làm sữa hạt công nghiệp hoặc máy xay nấu đa năng", "Máy pha cà phê"],
      correctAnswerIndex: 2
    }
  ],
  menu: [
    {
      question: "Khi xây dựng menu, nên phân chia nhóm thức uống như thế nào?",
      options: ["Chỉ bán một loại sữa", "Phân theo công dụng hoặc hương vị", "Bán tất cả các loại sữa có thể", "Tùy hứng mỗi ngày"],
      correctAnswerIndex: 1
    }
  ],
  costing: [
    {
      question: "Yếu tố nào quan trọng nhất khi tính giá vốn (costing)?",
      options: ["Chỉ tính tiền nguyên liệu", "Tính tất cả chi phí bao gồm nguyên liệu, bao bì, khấu hao, điện nước", "Tính theo giá thị trường", "Cảm tính"],
      correctAnswerIndex: 1
    }
  ],
  operations: [
    {
      question: "Để vận hành trơn tru, việc quan trọng cần làm vào đầu ca là gì?",
      options: ["Chờ khách đến mới bắt đầu chuẩn bị", "Kiểm tra nguyên liệu, máy móc và chuẩn bị sẵn các phần hạt đã ngâm", "Dọn dẹp sau", "Tính doanh thu"],
      correctAnswerIndex: 1
    }
  ],
  marketing: [
    {
      question: "Chiến lược marketing nào hiệu quả cho mô hình take-away mới mở?",
      options: ["Chỉ đợi khách vãng lai", "Phát tờ rơi, chạy khuyến mãi mua 1 tặng 1 trong ngày khai trương", "Chạy quảng cáo toàn quốc", "Không cần marketing"],
      correctAnswerIndex: 1
    }
  ],
  recipes: [
    {
      question: "Trong công thức sữa hạt, tỷ lệ hạt tạo béo và hạt tạo bột thường như thế nào để sữa cân bằng?",
      options: ["100% hạt tạo bột", "Kết hợp hài hòa giữa hạt tạo béo và hạt tạo bột theo tỷ lệ công thức", "100% hạt tạo béo", "Không quan trọng tỷ lệ"],
      correctAnswerIndex: 1
    }
  ],
  troubleshooting: [
    {
      question: "Nguyên nhân chính khiến sữa hạt bị tách nước là gì?",
      options: ["Do dùng quá nhiều đường", "Do nấu quá lửa, bảo quản sai cách hoặc tỷ lệ hạt chưa chuẩn", "Do dùng chai thủy tinh", "Do uống kèm đá"],
      correctAnswerIndex: 1
    }
  ]
};

export default function Quiz({ moduleId, currentUser }: { moduleId: string, currentUser: any }) {
  const [currentQuestionIdx, setCurrentQuestionIdx] = useState(0);
  const [selectedOption, setSelectedOption] = useState<number | null>(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [score, setScore] = useState(0);
  const [quizFinished, setQuizFinished] = useState(false);
  const [previousBestScore, setPreviousBestScore] = useState<number | null>(null);

  const questions = moduleQuizzes[moduleId] || [];

  useEffect(() => {
    // Reset state when module changes
    setCurrentQuestionIdx(0);
    setSelectedOption(null);
    setIsAnswered(false);
    setScore(0);
    setQuizFinished(false);

    // Fetch previous score if logged in
    if (currentUser && currentUser.role !== 'admin') {
      const fetchScore = async () => {
        const docRef = doc(db, "users", currentUser.id);
        const docSnap = await getDoc(docRef);
        if (docSnap.exists()) {
          const data = docSnap.data();
          if (data.quizResults && data.quizResults[moduleId] !== undefined) {
            setPreviousBestScore(data.quizResults[moduleId]);
          } else {
            setPreviousBestScore(null);
          }
        }
      };
      fetchScore();
    }
  }, [moduleId, currentUser]);

  if (questions.length === 0) return null;

  const handleOptionSelect = (idx: number) => {
    if (isAnswered) return;
    setSelectedOption(idx);
  };

  const handleCheckAnswer = () => {
    if (selectedOption === null) return;
    setIsAnswered(true);
    if (selectedOption === questions[currentQuestionIdx].correctAnswerIndex) {
      setScore(score + 1);
    }
  };

  const handleNext = async () => {
    if (currentQuestionIdx < questions.length - 1) {
      setCurrentQuestionIdx(currentQuestionIdx + 1);
      setSelectedOption(null);
      setIsAnswered(false);
    } else {
      setQuizFinished(true);
      const finalScore = score + (selectedOption === questions[currentQuestionIdx].correctAnswerIndex ? 1 : 0);
      
      if (currentUser && currentUser.role !== 'admin') {
        const docRef = doc(db, "users", currentUser.id);
        const newScore = Math.max(finalScore, previousBestScore || 0);
        try {
          await setDoc(docRef, {
            quizResults: {
              [moduleId]: newScore
            }
          }, { merge: true });
          setPreviousBestScore(newScore);
          toast.success("Đã lưu kết quả bài kiểm tra!");
        } catch (e) {
          console.error("Lỗi cập nhật điểm:", e);
        }
      }
    }
  };

  const handleRetry = () => {
    setCurrentQuestionIdx(0);
    setSelectedOption(null);
    setIsAnswered(false);
    setScore(0);
    setQuizFinished(false);
  };

  if (quizFinished) {
    return (
      <div className="mt-12 bg-white rounded-2xl border border-stone-200 p-8 text-center shadow-sm print:hidden">
        <h3 className="text-2xl font-bold text-stone-900 mb-4">Hoàn thành bài kiểm tra!</h3>
        <p className="text-lg text-stone-600 mb-6">
          Bạn trả lời đúng <span className="font-bold text-amber-600">{score}/{questions.length}</span> câu hỏi.
        </p>
        {previousBestScore !== null && (
          <p className="text-sm text-stone-500 mb-6">Điểm cao nhất của bạn: {previousBestScore}/{questions.length}</p>
        )}
        <button
          onClick={handleRetry}
          className="px-6 py-2.5 bg-amber-500 hover:bg-amber-600 text-white font-bold rounded-xl transition-colors shadow-sm"
        >
          Làm lại bài kiểm tra
        </button>
      </div>
    );
  }

  const q = questions[currentQuestionIdx];

  return (
    <div className="mt-16 bg-white rounded-2xl border border-stone-200 p-6 md:p-8 shadow-sm print:hidden">
      <div className="flex items-center justify-between mb-6">
        <h3 className="text-xl font-bold text-stone-900">Bài kiểm tra cuối Module</h3>
        <span className="text-sm font-bold text-stone-400 bg-stone-100 px-3 py-1 rounded-full">
          Câu {currentQuestionIdx + 1}/{questions.length}
        </span>
      </div>

      <div className="mb-8">
        <h4 className="text-lg font-bold text-stone-800 mb-6">{q.question}</h4>
        <div className="space-y-3">
          {q.options.map((opt, idx) => {
            let btnClass = "w-full text-left p-4 rounded-xl border transition-all duration-200 ";
            if (isAnswered) {
              if (idx === q.correctAnswerIndex) {
                btnClass += "bg-emerald-50 border-emerald-200 text-emerald-800";
              } else if (idx === selectedOption) {
                btnClass += "bg-rose-50 border-rose-200 text-rose-800";
              } else {
                btnClass += "bg-white border-stone-200 text-stone-500 opacity-50";
              }
            } else {
              if (idx === selectedOption) {
                btnClass += "bg-amber-50 border-amber-300 text-amber-800 shadow-sm ring-2 ring-amber-100";
              } else {
                btnClass += "bg-white border-stone-200 hover:border-amber-200 hover:bg-stone-50 text-stone-700";
              }
            }

            return (
              <button
                key={idx}
                disabled={isAnswered}
                onClick={() => handleOptionSelect(idx)}
                className={btnClass}
              >
                <div className="flex justify-between items-center">
                  <span className="font-medium">{opt}</span>
                  {isAnswered && idx === q.correctAnswerIndex && <CheckCircle2 size={20} className="text-emerald-500" />}
                  {isAnswered && idx === selectedOption && idx !== q.correctAnswerIndex && <XCircle size={20} className="text-rose-500" />}
                </div>
              </button>
            );
          })}
        </div>
      </div>

      <div className="flex justify-end border-t border-stone-100 pt-6">
        {!isAnswered ? (
          <button
            disabled={selectedOption === null}
            onClick={handleCheckAnswer}
            className="px-6 py-2.5 bg-stone-900 hover:bg-stone-800 text-white font-bold rounded-xl transition-colors shadow-sm disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Kiểm tra đáp án
          </button>
        ) : (
          <button
            onClick={handleNext}
            className="px-6 py-2.5 bg-amber-500 hover:bg-amber-600 text-white font-bold rounded-xl transition-colors shadow-sm"
          >
            {currentQuestionIdx < questions.length - 1 ? 'Câu tiếp theo' : 'Hoàn thành'}
          </button>
        )}
      </div>
    </div>
  );
}
